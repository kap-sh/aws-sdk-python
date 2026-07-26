"""Generated from Smithy shape ``com.amazonaws.emr#GetStudioSessionMappingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.session_mapping_detail


class GetStudioSessionMappingOutput(TypedDict, closed=True):
    session_mapping: NotRequired[
        "capo_emr.types.session_mapping_detail.SessionMappingDetail"
    ]
    """<p>The session mapping details for the specified Amazon EMR Studio and identity, including session policy ARN and creation time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStudioSessionMappingOutput) -> dict:
    out: dict = {}
    if "session_mapping" in value:
        import capo_emr.types.session_mapping_detail

        out["SessionMapping"] = (
            capo_emr.types.session_mapping_detail.serialize_aws_json_1_1(
                value["session_mapping"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStudioSessionMappingOutput:
    out: GetStudioSessionMappingOutput = {}  # type: ignore[typeddict-item]
    if "SessionMapping" in data:
        import capo_emr.types.session_mapping_detail

        out["session_mapping"] = (
            capo_emr.types.session_mapping_detail.deserialize_aws_json_1_1(
                data["SessionMapping"]
            )
        )
    return out
