"""Generated from Smithy shape ``com.amazonaws.support#DescribeCommunicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.communication_list
    import aws_sdk_support.types.next_token


class DescribeCommunicationsResponse(TypedDict):
    communications: NotRequired[
        "aws_sdk_support.types.communication_list.CommunicationList"
    ]
    """<p>The communications for the case.</p>"""
    next_token: NotRequired["aws_sdk_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCommunicationsResponse) -> dict:
    out: dict = {}
    if "communications" in value:
        import aws_sdk_support.types.communication_list

        out["communications"] = (
            aws_sdk_support.types.communication_list.serialize_aws_json_1_1(
                value["communications"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCommunicationsResponse:
    out: DescribeCommunicationsResponse = {}  # type: ignore[typeddict-item]
    if "communications" in data:
        import aws_sdk_support.types.communication_list

        out["communications"] = (
            aws_sdk_support.types.communication_list.deserialize_aws_json_1_1(
                data["communications"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
