"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Change``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change_specification
    import aws_sdk_cleanrooms.types.change_specification_type
    import aws_sdk_cleanrooms.types.change_type_list


class Change(TypedDict, closed=True):
    specification_type: (
        "aws_sdk_cleanrooms.types.change_specification_type.ChangeSpecificationType"
    )
    """<p>The type of specification for this change.</p>"""
    specification: "aws_sdk_cleanrooms.types.change_specification.ChangeSpecification"
    """<p>The specification details for this change.</p>"""
    types: "aws_sdk_cleanrooms.types.change_type_list.ChangeTypeList"
    """<p>The list of change types that were applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Change) -> dict:
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
    import aws_sdk_cleanrooms.types.change_type_list

    out["types"] = aws_sdk_cleanrooms.types.change_type_list.serialize_json(
        value["types"]
    )
    return out


def deserialize_json(data: dict) -> Change:
    out: Change = {}  # type: ignore[typeddict-item]
    if "specificationType" in data:
        import aws_sdk_cleanrooms.types.change_specification_type

        out["specification_type"] = (
            aws_sdk_cleanrooms.types.change_specification_type.deserialize_json(
                data["specificationType"]
            )
        )
    else:
        raise DeserializationError("Change.specification_type required")
    if "specification" in data:
        import aws_sdk_cleanrooms.types.change_specification

        out["specification"] = (
            aws_sdk_cleanrooms.types.change_specification.deserialize_json(
                data["specification"]
            )
        )
    else:
        raise DeserializationError("Change.specification required")
    if "types" in data:
        import aws_sdk_cleanrooms.types.change_type_list

        out["types"] = aws_sdk_cleanrooms.types.change_type_list.deserialize_json(
            data["types"]
        )
    else:
        raise DeserializationError("Change.types required")
    return out
