"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change_specification
    import aws_sdk_cleanrooms.types.change_specification_type


class ChangeInput(TypedDict, closed=True):
    specification_type: (
        "aws_sdk_cleanrooms.types.change_specification_type.ChangeSpecificationType"
    )
    """<p>The type of specification for the change. Currently supports <code>MEMBER</code> for member-related changes.</p>"""
    specification: "aws_sdk_cleanrooms.types.change_specification.ChangeSpecification"
    """<p>The specification details for the change. The structure depends on the specification type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.change_specification_type

    out["specificationType"] = (
        aws_sdk_cleanrooms.types.change_specification_type.serialize_json(
            value["specification_type"]
        )
    )
    import aws_sdk_cleanrooms.types.change_specification

    out["specification"] = aws_sdk_cleanrooms.types.change_specification.serialize_json(
        value["specification"]
    )
    return out


def deserialize_json(data: dict) -> ChangeInput:
    out: ChangeInput = {}  # type: ignore[typeddict-item]
    if "specificationType" in data:
        import aws_sdk_cleanrooms.types.change_specification_type

        out["specification_type"] = (
            aws_sdk_cleanrooms.types.change_specification_type.deserialize_json(
                data["specificationType"]
            )
        )
    else:
        raise DeserializationError("ChangeInput.specification_type required")
    if "specification" in data:
        import aws_sdk_cleanrooms.types.change_specification

        out["specification"] = (
            aws_sdk_cleanrooms.types.change_specification.deserialize_json(
                data["specification"]
            )
        )
    else:
        raise DeserializationError("ChangeInput.specification required")
    return out
