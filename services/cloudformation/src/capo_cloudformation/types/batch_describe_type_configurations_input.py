"""Generated from Smithy shape ``com.amazonaws.cloudformation#BatchDescribeTypeConfigurationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_configuration_identifiers


class BatchDescribeTypeConfigurationsInput(TypedDict, closed=True):
    type_configuration_identifiers: NotRequired[
        "capo_cloudformation.types.type_configuration_identifiers.TypeConfigurationIdentifiers"
    ]
    """<p>The list of identifiers for the desired extension configurations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDescribeTypeConfigurationsInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "type_configuration_identifiers" in value:
        import capo_cloudformation.types.type_configuration_identifiers

        capo_cloudformation.types.type_configuration_identifiers.serialize_query(
            value["type_configuration_identifiers"],
            pairs,
            f"{prefix}.TypeConfigurationIdentifiers",
        )


def deserialize_query(el: Element) -> BatchDescribeTypeConfigurationsInput:
    out: BatchDescribeTypeConfigurationsInput = {}  # type: ignore[typeddict-item]
    child_type_configuration_identifiers = el.find("TypeConfigurationIdentifiers")
    if child_type_configuration_identifiers is not None:
        import capo_cloudformation.types.type_configuration_identifiers

        out["type_configuration_identifiers"] = (
            capo_cloudformation.types.type_configuration_identifiers.deserialize_query(
                child_type_configuration_identifiers
            )
        )
    return out
