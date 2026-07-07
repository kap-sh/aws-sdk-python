"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MLMemberAbilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.custom_ml_member_abilities


class MLMemberAbilities(TypedDict, closed=True):
    custom_ml_member_abilities: (
        "aws_sdk_cleanrooms.types.custom_ml_member_abilities.CustomMLMemberAbilities"
    )
    """<p>The custom ML member abilities for a collaboration member. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLMemberAbilities) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.custom_ml_member_abilities

    out["customMLMemberAbilities"] = (
        aws_sdk_cleanrooms.types.custom_ml_member_abilities.serialize_json(
            value["custom_ml_member_abilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> MLMemberAbilities:
    out: MLMemberAbilities = {}  # type: ignore[typeddict-item]
    if "customMLMemberAbilities" in data:
        import aws_sdk_cleanrooms.types.custom_ml_member_abilities

        out["custom_ml_member_abilities"] = (
            aws_sdk_cleanrooms.types.custom_ml_member_abilities.deserialize_json(
                data["customMLMemberAbilities"]
            )
        )
    else:
        raise DeserializationError(
            "MLMemberAbilities.custom_ml_member_abilities required"
        )
    return out
