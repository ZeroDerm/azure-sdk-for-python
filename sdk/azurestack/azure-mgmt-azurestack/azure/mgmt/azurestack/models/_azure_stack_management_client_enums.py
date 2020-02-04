# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ProvisioningState(str, Enum):

    creating = "Creating"
    failed = "Failed"
    succeeded = "Succeeded"
    canceled = "Canceled"


class ComputeRole(str, Enum):

    none = "None"
    iaa_s = "IaaS"
    paa_s = "PaaS"


class OperatingSystem(str, Enum):

    none = "None"
    windows = "Windows"
    linux = "Linux"


class CompatibilityIssue(str, Enum):

    higher_device_version_required = "HigherDeviceVersionRequired"
    lower_device_version_required = "LowerDeviceVersionRequired"
    capacity_billing_model_required = "CapacityBillingModelRequired"
    pay_as_you_go_billing_model_required = "PayAsYouGoBillingModelRequired"
    development_billing_model_required = "DevelopmentBillingModelRequired"
    azure_ad_identity_system_required = "AzureADIdentitySystemRequired"
    adfs_identity_system_required = "ADFSIdentitySystemRequired"
    connection_to_internet_required = "ConnectionToInternetRequired"
    connection_to_azure_required = "ConnectionToAzureRequired"
    disconnected_environment_required = "DisconnectedEnvironmentRequired"


class Category(str, Enum):

    azure_ad = "AzureAD"
    adfs = "ADFS"


class Location(str, Enum):

    global_enum = "global"