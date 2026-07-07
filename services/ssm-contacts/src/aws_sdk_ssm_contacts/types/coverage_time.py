"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CoverageTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.hand_off_time


class CoverageTime(TypedDict, closed=True):
    start: NotRequired["aws_sdk_ssm_contacts.types.hand_off_time.HandOffTime"]
    """<p>Information about when the on-call rotation shift begins.</p>"""
    end: NotRequired["aws_sdk_ssm_contacts.types.hand_off_time.HandOffTime"]
    """<p>Information about when the on-call rotation shift ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageTime) -> dict:
    out: dict = {}
    if "start" in value:
        import aws_sdk_ssm_contacts.types.hand_off_time

        out["Start"] = aws_sdk_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(
            value["start"]
        )
    if "end" in value:
        import aws_sdk_ssm_contacts.types.hand_off_time

        out["End"] = aws_sdk_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(
            value["end"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CoverageTime:
    out: CoverageTime = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import aws_sdk_ssm_contacts.types.hand_off_time

        out["start"] = (
            aws_sdk_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(
                data["Start"]
            )
        )
    if "End" in data:
        import aws_sdk_ssm_contacts.types.hand_off_time

        out["end"] = aws_sdk_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(
            data["End"]
        )
    return out
