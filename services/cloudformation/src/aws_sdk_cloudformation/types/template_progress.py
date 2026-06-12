"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateProgress``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resources_failed
    import aws_sdk_cloudformation.types.resources_pending
    import aws_sdk_cloudformation.types.resources_processing
    import aws_sdk_cloudformation.types.resources_succeeded


class TemplateProgress(TypedDict):
    resources_succeeded: NotRequired[
        "aws_sdk_cloudformation.types.resources_succeeded.ResourcesSucceeded"
    ]
    """<p>The number of resources that succeeded the template generation.</p>"""
    resources_failed: NotRequired[
        "aws_sdk_cloudformation.types.resources_failed.ResourcesFailed"
    ]
    """<p>The number of resources that failed the template generation.</p>"""
    resources_processing: NotRequired[
        "aws_sdk_cloudformation.types.resources_processing.ResourcesProcessing"
    ]
    """<p>The number of resources that are in-process for the template generation.</p>"""
    resources_pending: NotRequired[
        "aws_sdk_cloudformation.types.resources_pending.ResourcesPending"
    ]
    """<p>The number of resources that are still pending the template generation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateProgress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resources_succeeded" in value:
        pairs.append(
            (f"{prefix}.ResourcesSucceeded", str(value["resources_succeeded"]))
        )
    if "resources_failed" in value:
        pairs.append((f"{prefix}.ResourcesFailed", str(value["resources_failed"])))
    if "resources_processing" in value:
        pairs.append(
            (f"{prefix}.ResourcesProcessing", str(value["resources_processing"]))
        )
    if "resources_pending" in value:
        pairs.append((f"{prefix}.ResourcesPending", str(value["resources_pending"])))


def deserialize_query(el: Element) -> TemplateProgress:
    out: TemplateProgress = {}  # type: ignore[typeddict-item]
    child_resources_succeeded = el.find("ResourcesSucceeded")
    if child_resources_succeeded is not None:
        out["resources_succeeded"] = int(child_resources_succeeded.text or "")
    child_resources_failed = el.find("ResourcesFailed")
    if child_resources_failed is not None:
        out["resources_failed"] = int(child_resources_failed.text or "")
    child_resources_processing = el.find("ResourcesProcessing")
    if child_resources_processing is not None:
        out["resources_processing"] = int(child_resources_processing.text or "")
    child_resources_pending = el.find("ResourcesPending")
    if child_resources_pending is not None:
        out["resources_pending"] = int(child_resources_pending.text or "")
    return out
