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

from msrest.paging import Paged


class BigDataPoolResourceInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BigDataPoolResourceInfo <azure.mgmt.synapse.models.BigDataPoolResourceInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BigDataPoolResourceInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(BigDataPoolResourceInfoPaged, self).__init__(*args, **kwargs)
class IpFirewallRuleInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IpFirewallRuleInfo <azure.mgmt.synapse.models.IpFirewallRuleInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IpFirewallRuleInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(IpFirewallRuleInfoPaged, self).__init__(*args, **kwargs)
class SqlPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPool <azure.mgmt.synapse.models.SqlPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolPaged, self).__init__(*args, **kwargs)
class RestorePointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RestorePoint <azure.mgmt.synapse.models.RestorePoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RestorePoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(RestorePointPaged, self).__init__(*args, **kwargs)
class ReplicationLinkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ReplicationLink <azure.mgmt.synapse.models.ReplicationLink>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ReplicationLink]'}
    }

    def __init__(self, *args, **kwargs):

        super(ReplicationLinkPaged, self).__init__(*args, **kwargs)
class SqlPoolOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolOperation <azure.mgmt.synapse.models.SqlPoolOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolOperationPaged, self).__init__(*args, **kwargs)
class SqlPoolUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolUsage <azure.mgmt.synapse.models.SqlPoolUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolUsagePaged, self).__init__(*args, **kwargs)
class SensitivityLabelPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SensitivityLabel <azure.mgmt.synapse.models.SensitivityLabel>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SensitivityLabel]'}
    }

    def __init__(self, *args, **kwargs):

        super(SensitivityLabelPaged, self).__init__(*args, **kwargs)
class SqlPoolSchemaPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolSchema <azure.mgmt.synapse.models.SqlPoolSchema>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolSchema]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolSchemaPaged, self).__init__(*args, **kwargs)
class SqlPoolTablePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolTable <azure.mgmt.synapse.models.SqlPoolTable>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolTable]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolTablePaged, self).__init__(*args, **kwargs)
class SqlPoolColumnPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolColumn <azure.mgmt.synapse.models.SqlPoolColumn>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolColumn]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolColumnPaged, self).__init__(*args, **kwargs)
class SqlPoolVulnerabilityAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlPoolVulnerabilityAssessment <azure.mgmt.synapse.models.SqlPoolVulnerabilityAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlPoolVulnerabilityAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlPoolVulnerabilityAssessmentPaged, self).__init__(*args, **kwargs)
class VulnerabilityAssessmentScanRecordPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VulnerabilityAssessmentScanRecord <azure.mgmt.synapse.models.VulnerabilityAssessmentScanRecord>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VulnerabilityAssessmentScanRecord]'}
    }

    def __init__(self, *args, **kwargs):

        super(VulnerabilityAssessmentScanRecordPaged, self).__init__(*args, **kwargs)
class WorkspacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Workspace <azure.mgmt.synapse.models.Workspace>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Workspace]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkspacePaged, self).__init__(*args, **kwargs)
class IntegrationRuntimeResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`IntegrationRuntimeResource <azure.mgmt.synapse.models.IntegrationRuntimeResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IntegrationRuntimeResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(IntegrationRuntimeResourcePaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.synapse.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.synapse.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkHubPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkHub <azure.mgmt.synapse.models.PrivateLinkHub>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkHub]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkHubPaged, self).__init__(*args, **kwargs)
