"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceDriftIgnoredAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.drift_ignored_reason
    import aws_sdk_cloudformation.types.resource_property_path


class ResourceDriftIgnoredAttribute(TypedDict):
    path: NotRequired[
        "aws_sdk_cloudformation.types.resource_property_path.ResourcePropertyPath"
    ]
    """<p>Path of the resource attribute for which drift was ignored.</p>"""
    reason: NotRequired[
        "aws_sdk_cloudformation.types.drift_ignored_reason.DriftIgnoredReason"
    ]
    """<p>Reason why drift was ignored for the attribute, can have 2 possible values:</p> <ul> <li> <p> <code>WRITE_ONLY_PROPERTY</code> - Property is not included in read response for the resource’s live state.</p> </li> <li> <p> <code>MANAGED_BY_AWS</code> - Property is managed by an Amazon Web Services service and is expected to be dynamically modified.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceDriftIgnoredAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "path" in value:
        pairs.append((f"{prefix}.Path", str(value["path"])))
    if "reason" in value:
        import aws_sdk_cloudformation.types.drift_ignored_reason

        aws_sdk_cloudformation.types.drift_ignored_reason.serialize_query(
            value["reason"], pairs, f"{prefix}.Reason"
        )


def deserialize_query(el: Element) -> ResourceDriftIgnoredAttribute:
    out: ResourceDriftIgnoredAttribute = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_reason = el.find("Reason")
    if child_reason is not None:
        import aws_sdk_cloudformation.types.drift_ignored_reason

        out["reason"] = (
            aws_sdk_cloudformation.types.drift_ignored_reason.deserialize_query(
                child_reason
            )
        )
    return out
