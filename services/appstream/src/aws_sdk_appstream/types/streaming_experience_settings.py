"""Generated from Smithy shape ``com.amazonaws.appstream#StreamingExperienceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.preferred_protocol


class StreamingExperienceSettings(TypedDict):
    preferred_protocol: NotRequired[
        "aws_sdk_appstream.types.preferred_protocol.PreferredProtocol"
    ]
    """<p>The preferred protocol that you want to use while streaming your application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingExperienceSettings) -> dict:
    out: dict = {}
    if "preferred_protocol" in value:
        import aws_sdk_appstream.types.preferred_protocol

        out["PreferredProtocol"] = (
            aws_sdk_appstream.types.preferred_protocol.serialize_aws_json_1_1(
                value["preferred_protocol"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamingExperienceSettings:
    out: StreamingExperienceSettings = {}  # type: ignore[typeddict-item]
    if "PreferredProtocol" in data:
        import aws_sdk_appstream.types.preferred_protocol

        out["preferred_protocol"] = (
            aws_sdk_appstream.types.preferred_protocol.deserialize_aws_json_1_1(
                data["PreferredProtocol"]
            )
        )
    return out
