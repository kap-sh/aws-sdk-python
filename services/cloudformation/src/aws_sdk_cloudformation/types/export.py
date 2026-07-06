"""Generated from Smithy shape ``com.amazonaws.cloudformation#Export``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.export_name
    import aws_sdk_cloudformation.types.export_value
    import aws_sdk_cloudformation.types.stack_id


class Export(TypedDict, closed=True):
    exporting_stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The stack that contains the exported output name and value.</p>"""
    name: NotRequired["aws_sdk_cloudformation.types.export_name.ExportName"]
    """<p>The name of exported output value. Use this name and the <code>Fn::ImportValue</code> function to import the associated value into other stacks. The name is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.</p>"""
    value: NotRequired["aws_sdk_cloudformation.types.export_value.ExportValue"]
    """<p>The value of the exported output, such as a resource physical ID. This value is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Export, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "exporting_stack_id" in value:
        pairs.append((f"{prefix}.ExportingStackId", str(value["exporting_stack_id"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> Export:
    out: Export = {}  # type: ignore[typeddict-item]
    child_exporting_stack_id = el.find("ExportingStackId")
    if child_exporting_stack_id is not None:
        out["exporting_stack_id"] = str(child_exporting_stack_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
