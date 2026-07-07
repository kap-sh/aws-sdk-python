"""Generated from Smithy shape ``com.amazonaws.shield#Mitigation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.string


class Mitigation(TypedDict, closed=True):
    mitigation_name: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The name of the mitigation taken for this attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mitigation) -> dict:
    out: dict = {}
    if "mitigation_name" in value:
        out["MitigationName"] = value["mitigation_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Mitigation:
    out: Mitigation = {}  # type: ignore[typeddict-item]
    if "MitigationName" in data:
        out["mitigation_name"] = data["MitigationName"]
    return out
