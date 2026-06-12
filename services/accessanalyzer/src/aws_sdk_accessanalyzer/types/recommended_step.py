"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RecommendedStep``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.unused_permissions_recommended_step


class _RecommendedStep_unusedPermissionsRecommendedStep(TypedDict):
    unusedPermissionsRecommendedStep: "aws_sdk_accessanalyzer.types.unused_permissions_recommended_step.UnusedPermissionsRecommendedStep"


RecommendedStep: TypeAlias = _RecommendedStep_unusedPermissionsRecommendedStep


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedStep) -> dict:
    if "unusedPermissionsRecommendedStep" in value:
        import aws_sdk_accessanalyzer.types.unused_permissions_recommended_step

        return {
            "unusedPermissionsRecommendedStep": aws_sdk_accessanalyzer.types.unused_permissions_recommended_step.serialize_json(
                value["unusedPermissionsRecommendedStep"]
            )
        }
    else:
        raise SerializationError("RecommendedStep: no variant present")


def deserialize_json(data: dict) -> RecommendedStep:
    if "unusedPermissionsRecommendedStep" in data:
        import aws_sdk_accessanalyzer.types.unused_permissions_recommended_step

        return {
            "unusedPermissionsRecommendedStep": aws_sdk_accessanalyzer.types.unused_permissions_recommended_step.deserialize_json(
                data["unusedPermissionsRecommendedStep"]
            )
        }
    else:
        raise DeserializationError("RecommendedStep: no recognized variant key")
