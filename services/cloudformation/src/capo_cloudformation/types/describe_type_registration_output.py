"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeTypeRegistrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.description
    import capo_cloudformation.types.registration_status
    import capo_cloudformation.types.type_arn


class DescribeTypeRegistrationOutput(TypedDict, closed=True):
    progress_status: NotRequired[
        "capo_cloudformation.types.registration_status.RegistrationStatus"
    ]
    """<p>The current status of the extension registration request.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The description of the extension registration request.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension being registered.</p> <p>For registration requests with a <code>ProgressStatus</code> of other than <code>COMPLETE</code>, this will be <code>null</code>.</p>"""
    type_version_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of this specific version of the extension being registered.</p> <p>For registration requests with a <code>ProgressStatus</code> of other than <code>COMPLETE</code>, this will be <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTypeRegistrationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "progress_status" in value:
        import capo_cloudformation.types.registration_status

        capo_cloudformation.types.registration_status.serialize_query(
            value["progress_status"], pairs, f"{key_prefix}ProgressStatus"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "type_version_arn" in value:
        pairs.append((f"{key_prefix}TypeVersionArn", str(value["type_version_arn"])))


def deserialize_query(el: Element) -> DescribeTypeRegistrationOutput:
    out: DescribeTypeRegistrationOutput = {}  # type: ignore[typeddict-item]
    child_progress_status = el.find("ProgressStatus")
    if child_progress_status is not None:
        import capo_cloudformation.types.registration_status

        out["progress_status"] = (
            capo_cloudformation.types.registration_status.deserialize_query(
                child_progress_status
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_type_version_arn = el.find("TypeVersionArn")
    if child_type_version_arn is not None:
        out["type_version_arn"] = str(child_type_version_arn.text or "")
    return out
