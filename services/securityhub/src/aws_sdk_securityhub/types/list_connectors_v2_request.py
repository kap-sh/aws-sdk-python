"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConnectorsV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.connector_provider_name
    import aws_sdk_securityhub.types.connector_status
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class ListConnectorsV2Request(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token per the Amazon Web Services Pagination standard</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned.</p>"""
    provider_name: NotRequired[
        "aws_sdk_securityhub.types.connector_provider_name.ConnectorProviderName"
    ]
    """<p>The name of the third-party provider.</p>"""
    connector_status: NotRequired[
        "aws_sdk_securityhub.types.connector_status.ConnectorStatus"
    ]
    """<p>The status for the connectorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorsV2Request:
    out: ListConnectorsV2Request = {}  # type: ignore[typeddict-item]
    return out
