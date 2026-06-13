"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.implementation_identifier_filter_list
    import aws_sdk_controlcatalog.types.implementation_type_filter_list


class ImplementationFilter(TypedDict):
    types: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_type_filter_list.ImplementationTypeFilterList"
    ]
    """<p>A list of implementation types that can serve as filters. For example, you can filter for controls implemented as Amazon Web Services Config Rules by specifying AWS::Config::ConfigRule as a type.</p>"""
    identifiers: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_identifier_filter_list.ImplementationIdentifierFilterList"
    ]
    """<p>A list of service-specific identifiers that can serve as filters. For example, you can filter for controls with specific Amazon Web Services Config Rule IDs or Security Hub Control IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationFilter) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_controlcatalog.types.implementation_type_filter_list

        out["Types"] = (
            aws_sdk_controlcatalog.types.implementation_type_filter_list.serialize_json(
                value["types"]
            )
        )
    if "identifiers" in value:
        import aws_sdk_controlcatalog.types.implementation_identifier_filter_list

        out["Identifiers"] = (
            aws_sdk_controlcatalog.types.implementation_identifier_filter_list.serialize_json(
                value["identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImplementationFilter:
    out: ImplementationFilter = {}  # type: ignore[typeddict-item]
    if "Types" in data:
        import aws_sdk_controlcatalog.types.implementation_type_filter_list

        out["types"] = (
            aws_sdk_controlcatalog.types.implementation_type_filter_list.deserialize_json(
                data["Types"]
            )
        )
    if "Identifiers" in data:
        import aws_sdk_controlcatalog.types.implementation_identifier_filter_list

        out["identifiers"] = (
            aws_sdk_controlcatalog.types.implementation_identifier_filter_list.deserialize_json(
                data["Identifiers"]
            )
        )
    return out
