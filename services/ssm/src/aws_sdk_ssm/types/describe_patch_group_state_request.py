"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchGroupStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_group


class DescribePatchGroupStateRequest(TypedDict, closed=True):
    patch_group: "aws_sdk_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group whose patch snapshot should be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchGroupStateRequest) -> dict:
    out: dict = {}
    out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchGroupStateRequest:
    out: DescribePatchGroupStateRequest = {}  # type: ignore[typeddict-item]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    else:
        raise DeserializationError(
            "DescribePatchGroupStateRequest.patch_group required"
        )
    return out
