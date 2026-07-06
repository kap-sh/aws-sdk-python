"""Generated from Smithy shape ``com.amazonaws.ssm#GetDefaultPatchBaselineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.operating_system


class GetDefaultPatchBaselineRequest(TypedDict, closed=True):
    operating_system: NotRequired["aws_sdk_ssm.types.operating_system.OperatingSystem"]
    """<p>Returns the default patch baseline for the specified operating system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDefaultPatchBaselineRequest) -> dict:
    out: dict = {}
    if "operating_system" in value:
        import aws_sdk_ssm.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_ssm.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDefaultPatchBaselineRequest:
    out: GetDefaultPatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if "OperatingSystem" in data:
        import aws_sdk_ssm.types.operating_system

        out["operating_system"] = (
            aws_sdk_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
