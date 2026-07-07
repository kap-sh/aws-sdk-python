"""Generated from Smithy shape ``com.amazonaws.cloudformation#Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.description
    import aws_sdk_cloudformation.types.export_name
    import aws_sdk_cloudformation.types.output_key
    import aws_sdk_cloudformation.types.output_value


class Output(TypedDict, closed=True):
    output_key: NotRequired["aws_sdk_cloudformation.types.output_key.OutputKey"]
    """<p>The key associated with the output.</p>"""
    output_value: NotRequired["aws_sdk_cloudformation.types.output_value.OutputValue"]
    """<p>The value associated with the output.</p>"""
    description: NotRequired["aws_sdk_cloudformation.types.description.Description"]
    """<p>User defined description associated with the output.</p>"""
    export_name: NotRequired["aws_sdk_cloudformation.types.export_name.ExportName"]
    """<p>The name of the export associated with the output.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Output, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "output_key" in value:
        pairs.append((f"{prefix}.OutputKey", str(value["output_key"])))
    if "output_value" in value:
        pairs.append((f"{prefix}.OutputValue", str(value["output_value"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "export_name" in value:
        pairs.append((f"{prefix}.ExportName", str(value["export_name"])))


def deserialize_query(el: Element) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    child_output_key = el.find("OutputKey")
    if child_output_key is not None:
        out["output_key"] = str(child_output_key.text or "")
    child_output_value = el.find("OutputValue")
    if child_output_value is not None:
        out["output_value"] = str(child_output_value.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_export_name = el.find("ExportName")
    if child_export_name is not None:
        out["export_name"] = str(child_export_name.text or "")
    return out
