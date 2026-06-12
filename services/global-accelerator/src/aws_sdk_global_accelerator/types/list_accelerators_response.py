"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListAcceleratorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.accelerators
    import aws_sdk_global_accelerator.types.generic_string


class ListAcceleratorsResponse(TypedDict):
    accelerators: NotRequired[
        "aws_sdk_global_accelerator.types.accelerators.Accelerators"
    ]
    """<p>The list of accelerators for a customer account.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcceleratorsResponse) -> dict:
    out: dict = {}
    if "accelerators" in value:
        import aws_sdk_global_accelerator.types.accelerators

        out["Accelerators"] = (
            aws_sdk_global_accelerator.types.accelerators.serialize_aws_json_1_1(
                value["accelerators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcceleratorsResponse:
    out: ListAcceleratorsResponse = {}  # type: ignore[typeddict-item]
    if "Accelerators" in data:
        import aws_sdk_global_accelerator.types.accelerators

        out["accelerators"] = (
            aws_sdk_global_accelerator.types.accelerators.deserialize_aws_json_1_1(
                data["Accelerators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
