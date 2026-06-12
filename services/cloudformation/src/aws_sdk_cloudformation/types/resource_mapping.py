"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_location


class ResourceMapping(TypedDict):
    source: NotRequired[
        "aws_sdk_cloudformation.types.resource_location.ResourceLocation"
    ]
    """<p>The source stack <code>StackName</code> and <code>LogicalResourceId</code> for the resource being refactored.</p>"""
    destination: NotRequired[
        "aws_sdk_cloudformation.types.resource_location.ResourceLocation"
    ]
    """<p>The destination stack <code>StackName</code> and <code>LogicalResourceId</code> for the resource being refactored.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source" in value:
        import aws_sdk_cloudformation.types.resource_location

        aws_sdk_cloudformation.types.resource_location.serialize_query(
            value["source"], pairs, f"{prefix}.Source"
        )
    if "destination" in value:
        import aws_sdk_cloudformation.types.resource_location

        aws_sdk_cloudformation.types.resource_location.serialize_query(
            value["destination"], pairs, f"{prefix}.Destination"
        )


def deserialize_query(el: Element) -> ResourceMapping:
    out: ResourceMapping = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import aws_sdk_cloudformation.types.resource_location

        out["source"] = (
            aws_sdk_cloudformation.types.resource_location.deserialize_query(
                child_source
            )
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import aws_sdk_cloudformation.types.resource_location

        out["destination"] = (
            aws_sdk_cloudformation.types.resource_location.deserialize_query(
                child_destination
            )
        )
    return out
