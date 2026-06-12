"""Generated from Smithy shape ``com.amazonaws.cloudformation#ParameterConstraints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.allowed_values


class ParameterConstraints(TypedDict):
    allowed_values: NotRequired[
        "aws_sdk_cloudformation.types.allowed_values.AllowedValues"
    ]
    """<p>A list of values that are permitted for a parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterConstraints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allowed_values" in value:
        import aws_sdk_cloudformation.types.allowed_values

        aws_sdk_cloudformation.types.allowed_values.serialize_query(
            value["allowed_values"], pairs, f"{prefix}.AllowedValues"
        )


def deserialize_query(el: Element) -> ParameterConstraints:
    out: ParameterConstraints = {}  # type: ignore[typeddict-item]
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        import aws_sdk_cloudformation.types.allowed_values

        out["allowed_values"] = (
            aws_sdk_cloudformation.types.allowed_values.deserialize_query(
                child_allowed_values
            )
        )
    return out
