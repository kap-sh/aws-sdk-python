"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.context_attribute_list
    import aws_sdk_rds.types.issue_details
    import aws_sdk_rds.types.recommended_action_parameter_list
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.string_list


class RecommendedAction(TypedDict, closed=True):
    action_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The unique identifier of the recommended action.</p>"""
    title: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A short description to summarize the action. The description might contain markdown.</p>"""
    description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A detailed description of the action. The description might contain markdown.</p>"""
    operation: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An API operation for the action.</p>"""
    parameters: NotRequired[
        "aws_sdk_rds.types.recommended_action_parameter_list.RecommendedActionParameterList"
    ]
    """<p>The parameters for the API operation.</p>"""
    apply_modes: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>The methods to apply the recommended action.</p> <p>Valid values:</p> <ul> <li> <p> <code>manual</code> - The action requires you to resolve the recommendation manually.</p> </li> <li> <p> <code>immediately</code> - The action is applied immediately.</p> </li> <li> <p> <code>next-maintainance-window</code> - The action is applied during the next scheduled maintainance.</p> </li> </ul>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the action.</p> <ul> <li> <p> <code>ready</code> </p> </li> <li> <p> <code>applied</code> </p> </li> <li> <p> <code>scheduled</code> </p> </li> <li> <p> <code>resolved</code> </p> </li> </ul>"""
    issue_details: NotRequired["aws_sdk_rds.types.issue_details.IssueDetails"]
    """<p>The details of the issue.</p>"""
    context_attributes: NotRequired[
        "aws_sdk_rds.types.context_attribute_list.ContextAttributeList"
    ]
    """<p>The supporting attributes to explain the recommended action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action_id" in value:
        pairs.append((f"{prefix}.ActionId", str(value["action_id"])))
    if "title" in value:
        pairs.append((f"{prefix}.Title", str(value["title"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "operation" in value:
        pairs.append((f"{prefix}.Operation", str(value["operation"])))
    if "parameters" in value:
        import aws_sdk_rds.types.recommended_action_parameter_list

        aws_sdk_rds.types.recommended_action_parameter_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )
    if "apply_modes" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["apply_modes"], pairs, f"{prefix}.ApplyModes"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "issue_details" in value:
        import aws_sdk_rds.types.issue_details

        aws_sdk_rds.types.issue_details.serialize_query(
            value["issue_details"], pairs, f"{prefix}.IssueDetails"
        )
    if "context_attributes" in value:
        import aws_sdk_rds.types.context_attribute_list

        aws_sdk_rds.types.context_attribute_list.serialize_query(
            value["context_attributes"], pairs, f"{prefix}.ContextAttributes"
        )


def deserialize_query(el: Element) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_title = el.find("Title")
    if child_title is not None:
        out["title"] = str(child_title.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_operation = el.find("Operation")
    if child_operation is not None:
        out["operation"] = str(child_operation.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_rds.types.recommended_action_parameter_list

        out["parameters"] = (
            aws_sdk_rds.types.recommended_action_parameter_list.deserialize_query(
                child_parameters
            )
        )
    child_apply_modes = el.find("ApplyModes")
    if child_apply_modes is not None:
        import aws_sdk_rds.types.string_list

        out["apply_modes"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_apply_modes
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_issue_details = el.find("IssueDetails")
    if child_issue_details is not None:
        import aws_sdk_rds.types.issue_details

        out["issue_details"] = aws_sdk_rds.types.issue_details.deserialize_query(
            child_issue_details
        )
    child_context_attributes = el.find("ContextAttributes")
    if child_context_attributes is not None:
        import aws_sdk_rds.types.context_attribute_list

        out["context_attributes"] = (
            aws_sdk_rds.types.context_attribute_list.deserialize_query(
                child_context_attributes
            )
        )
    return out
