"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateSummaryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.treat_unrecognized_resource_types_as_warnings


class TemplateSummaryConfig(TypedDict, closed=True):
    treat_unrecognized_resource_types_as_warnings: NotRequired[
        "aws_sdk_cloudformation.types.treat_unrecognized_resource_types_as_warnings.TreatUnrecognizedResourceTypesAsWarnings"
    ]
    """<p>If set to <code>True</code>, any unrecognized resource types generate warnings and not an error. Any unrecognized resource types are returned in the <code>Warnings</code> output parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateSummaryConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "treat_unrecognized_resource_types_as_warnings" in value:
        pairs.append(
            (
                f"{prefix}.TreatUnrecognizedResourceTypesAsWarnings",
                "true"
                if value["treat_unrecognized_resource_types_as_warnings"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> TemplateSummaryConfig:
    out: TemplateSummaryConfig = {}  # type: ignore[typeddict-item]
    child_treat_unrecognized_resource_types_as_warnings = el.find(
        "TreatUnrecognizedResourceTypesAsWarnings"
    )
    if child_treat_unrecognized_resource_types_as_warnings is not None:
        out["treat_unrecognized_resource_types_as_warnings"] = (
            child_treat_unrecognized_resource_types_as_warnings.text or ""
        ).lower() == "true"
    return out
