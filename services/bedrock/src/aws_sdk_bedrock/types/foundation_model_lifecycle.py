"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelLifecycle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.foundation_model_lifecycle_status
    import aws_sdk_bedrock.types.timestamp


class FoundationModelLifecycle(TypedDict):
    status: "aws_sdk_bedrock.types.foundation_model_lifecycle_status.FoundationModelLifecycleStatus"
    """<p>Specifies whether a model version is available (<code>ACTIVE</code>) or deprecated (<code>LEGACY</code>.</p>"""
    start_of_life_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Launch time when the model first becomes available</p>"""
    end_of_life_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Time when the model is no longer available for use</p>"""
    legacy_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Time when the model enters legacy state. Models in legacy state can still be used, but users should plan to transition to an Active model before the end of life time</p>"""
    public_extended_access_time: NotRequired[
        "aws_sdk_bedrock.types.timestamp.Timestamp"
    ]
    """<p>Public extended access portion of the legacy period, when users should expect higher pricing</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelLifecycle) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.foundation_model_lifecycle_status

    out["status"] = (
        aws_sdk_bedrock.types.foundation_model_lifecycle_status.serialize_json(
            value["status"]
        )
    )
    if "start_of_life_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["startOfLifeTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["start_of_life_time"]
        )
    if "end_of_life_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["endOfLifeTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["end_of_life_time"]
        )
    if "legacy_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["legacyTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["legacy_time"]
        )
    if "public_extended_access_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["publicExtendedAccessTime"] = (
            aws_sdk_bedrock.types.timestamp.serialize_json(
                value["public_extended_access_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> FoundationModelLifecycle:
    out: FoundationModelLifecycle = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock.types.foundation_model_lifecycle_status

        out["status"] = (
            aws_sdk_bedrock.types.foundation_model_lifecycle_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("FoundationModelLifecycle.status required")
    if "startOfLifeTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["start_of_life_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["startOfLifeTime"]
        )
    if "endOfLifeTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["end_of_life_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["endOfLifeTime"]
        )
    if "legacyTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["legacy_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["legacyTime"]
        )
    if "publicExtendedAccessTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["public_extended_access_time"] = (
            aws_sdk_bedrock.types.timestamp.deserialize_json(
                data["publicExtendedAccessTime"]
            )
        )
    return out
