"""Generated from Smithy shape ``com.amazonaws.cloudformation#Warnings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.resource_types


class Warnings(TypedDict, closed=True):
    unrecognized_resource_types: NotRequired[
        "capo_cloudformation.types.resource_types.ResourceTypes"
    ]
    """<p>A list of all of the unrecognized resource types. This is only returned if the <code>TemplateSummaryConfig</code> parameter has the <code>TreatUnrecognizedResourceTypesAsWarning</code> configuration set to <code>True</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Warnings, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "unrecognized_resource_types" in value:
        import capo_cloudformation.types.resource_types

        capo_cloudformation.types.resource_types.serialize_query(
            value["unrecognized_resource_types"],
            pairs,
            f"{key_prefix}UnrecognizedResourceTypes",
        )


def deserialize_query(el: Element) -> Warnings:
    out: Warnings = {}  # type: ignore[typeddict-item]
    child_unrecognized_resource_types = el.find("UnrecognizedResourceTypes")
    if child_unrecognized_resource_types is not None:
        import capo_cloudformation.types.resource_types

        out["unrecognized_resource_types"] = (
            capo_cloudformation.types.resource_types.deserialize_query(
                child_unrecognized_resource_types
            )
        )
    return out
