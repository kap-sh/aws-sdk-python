"""Generated from Smithy shape ``com.amazonaws.connectcases#ParentChildFieldOptionsMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.parent_child_field_option_value
    import aws_sdk_connectcases.types.parent_child_field_option_value_list


class ParentChildFieldOptionsMapping(TypedDict):
    parent_field_option_value: "aws_sdk_connectcases.types.parent_child_field_option_value.ParentChildFieldOptionValue"
    """<p>The value in the parent field.</p>"""
    child_field_option_values: "aws_sdk_connectcases.types.parent_child_field_option_value_list.ParentChildFieldOptionValueList"
    """<p>A list of allowed values in the child field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentChildFieldOptionsMapping) -> dict:
    out: dict = {}
    out["parentFieldOptionValue"] = value["parent_field_option_value"]
    import aws_sdk_connectcases.types.parent_child_field_option_value_list

    out["childFieldOptionValues"] = (
        aws_sdk_connectcases.types.parent_child_field_option_value_list.serialize_json(
            value["child_field_option_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ParentChildFieldOptionsMapping:
    out: ParentChildFieldOptionsMapping = {}  # type: ignore[typeddict-item]
    if "parentFieldOptionValue" in data:
        out["parent_field_option_value"] = data["parentFieldOptionValue"]
    else:
        raise DeserializationError(
            "ParentChildFieldOptionsMapping.parent_field_option_value required"
        )
    if "childFieldOptionValues" in data:
        import aws_sdk_connectcases.types.parent_child_field_option_value_list

        out["child_field_option_values"] = (
            aws_sdk_connectcases.types.parent_child_field_option_value_list.deserialize_json(
                data["childFieldOptionValues"]
            )
        )
    else:
        raise DeserializationError(
            "ParentChildFieldOptionsMapping.child_field_option_values required"
        )
    return out
