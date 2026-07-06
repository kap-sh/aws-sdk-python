"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.identifier_list
    import aws_sdk_amplifyuibuilder.types.predicate
    import aws_sdk_amplifyuibuilder.types.sort_property_list


class ComponentDataConfiguration(TypedDict, closed=True):
    model: "str"
    """<p>The name of the data model to use to bind data to a component.</p>"""
    sort: NotRequired[
        "aws_sdk_amplifyuibuilder.types.sort_property_list.SortPropertyList"
    ]
    """<p>Describes how to sort the component's properties.</p>"""
    predicate: NotRequired["aws_sdk_amplifyuibuilder.types.predicate.Predicate"]
    """<p>Represents the conditional logic to use when binding data to a component. Use this property to retrieve only a subset of the data in a collection.</p>"""
    identifiers: NotRequired[
        "aws_sdk_amplifyuibuilder.types.identifier_list.IdentifierList"
    ]
    """<p>A list of IDs to use to bind data to a component. Use this property to bind specifically chosen data, rather than data retrieved from a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentDataConfiguration) -> dict:
    out: dict = {}
    out["model"] = value["model"]
    if "sort" in value:
        import aws_sdk_amplifyuibuilder.types.sort_property_list

        out["sort"] = aws_sdk_amplifyuibuilder.types.sort_property_list.serialize_json(
            value["sort"]
        )
    if "predicate" in value:
        import aws_sdk_amplifyuibuilder.types.predicate

        out["predicate"] = aws_sdk_amplifyuibuilder.types.predicate.serialize_json(
            value["predicate"]
        )
    if "identifiers" in value:
        import aws_sdk_amplifyuibuilder.types.identifier_list

        out["identifiers"] = (
            aws_sdk_amplifyuibuilder.types.identifier_list.serialize_json(
                value["identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentDataConfiguration:
    out: ComponentDataConfiguration = {}  # type: ignore[typeddict-item]
    if "model" in data:
        out["model"] = data["model"]
    else:
        raise DeserializationError("ComponentDataConfiguration.model required")
    if "sort" in data:
        import aws_sdk_amplifyuibuilder.types.sort_property_list

        out["sort"] = (
            aws_sdk_amplifyuibuilder.types.sort_property_list.deserialize_json(
                data["sort"]
            )
        )
    if "predicate" in data:
        import aws_sdk_amplifyuibuilder.types.predicate

        out["predicate"] = aws_sdk_amplifyuibuilder.types.predicate.deserialize_json(
            data["predicate"]
        )
    if "identifiers" in data:
        import aws_sdk_amplifyuibuilder.types.identifier_list

        out["identifiers"] = (
            aws_sdk_amplifyuibuilder.types.identifier_list.deserialize_json(
                data["identifiers"]
            )
        )
    return out
