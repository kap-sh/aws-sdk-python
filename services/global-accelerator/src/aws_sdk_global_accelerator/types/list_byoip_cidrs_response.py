"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListByoipCidrsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.byoip_cidrs
    import aws_sdk_global_accelerator.types.generic_string


class ListByoipCidrsResponse(TypedDict):
    byoip_cidrs: NotRequired["aws_sdk_global_accelerator.types.byoip_cidrs.ByoipCidrs"]
    """<p>Information about your address ranges.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListByoipCidrsResponse) -> dict:
    out: dict = {}
    if "byoip_cidrs" in value:
        import aws_sdk_global_accelerator.types.byoip_cidrs

        out["ByoipCidrs"] = (
            aws_sdk_global_accelerator.types.byoip_cidrs.serialize_aws_json_1_1(
                value["byoip_cidrs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListByoipCidrsResponse:
    out: ListByoipCidrsResponse = {}  # type: ignore[typeddict-item]
    if "ByoipCidrs" in data:
        import aws_sdk_global_accelerator.types.byoip_cidrs

        out["byoip_cidrs"] = (
            aws_sdk_global_accelerator.types.byoip_cidrs.deserialize_aws_json_1_1(
                data["ByoipCidrs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
