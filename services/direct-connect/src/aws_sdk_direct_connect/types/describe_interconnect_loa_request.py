"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeInterconnectLoaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.interconnect_id
    import aws_sdk_direct_connect.types.loa_content_type
    import aws_sdk_direct_connect.types.provider_name


class DescribeInterconnectLoaRequest(TypedDict, closed=True):
    interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId"
    """<p>The ID of the interconnect.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>"""
    loa_content_type: NotRequired[
        "aws_sdk_direct_connect.types.loa_content_type.LoaContentType"
    ]
    """<p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInterconnectLoaRequest) -> dict:
    out: dict = {}
    out["interconnectId"] = value["interconnect_id"]
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "loa_content_type" in value:
        import aws_sdk_direct_connect.types.loa_content_type

        out["loaContentType"] = (
            aws_sdk_direct_connect.types.loa_content_type.serialize_aws_json_1_1(
                value["loa_content_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInterconnectLoaRequest:
    out: DescribeInterconnectLoaRequest = {}  # type: ignore[typeddict-item]
    if "interconnectId" in data:
        out["interconnect_id"] = data["interconnectId"]
    else:
        raise DeserializationError(
            "DescribeInterconnectLoaRequest.interconnect_id required"
        )
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "loaContentType" in data:
        import aws_sdk_direct_connect.types.loa_content_type

        out["loa_content_type"] = (
            aws_sdk_direct_connect.types.loa_content_type.deserialize_aws_json_1_1(
                data["loaContentType"]
            )
        )
    return out
