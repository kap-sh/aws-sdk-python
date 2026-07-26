"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_category_list
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_name
    import capo_socialmessaging.types.meta_flow_status
    import capo_socialmessaging.types.validation_error_list


class MetaFlowSummary(TypedDict, closed=True):
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow assigned by Meta.</p>"""
    flow_name: "capo_socialmessaging.types.meta_flow_name.MetaFlowName"
    """<p>The name of the Flow.</p>"""
    flow_status: "capo_socialmessaging.types.meta_flow_status.MetaFlowStatus"
    """<p>The lifecycle status of the Flow (DRAFT, PUBLISHED, DEPRECATED, BLOCKED, or THROTTLED).</p>"""
    flow_categories: (
        "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    )
    """<p>The categories that classify the business purpose of the Flow.</p>"""
    validation_errors: (
        "capo_socialmessaging.types.validation_error_list.ValidationErrorList"
    )
    """<p>A list of validation errors from Meta, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowSummary) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    out["flowName"] = value["flow_name"]
    out["flowStatus"] = value["flow_status"]
    import capo_socialmessaging.types.meta_flow_category_list

    out["flowCategories"] = (
        capo_socialmessaging.types.meta_flow_category_list.serialize_json(
            value["flow_categories"]
        )
    )
    import capo_socialmessaging.types.validation_error_list

    out["validationErrors"] = (
        capo_socialmessaging.types.validation_error_list.serialize_json(
            value["validation_errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> MetaFlowSummary:
    out: MetaFlowSummary = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("MetaFlowSummary.flow_id required")
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("MetaFlowSummary.flow_name required")
    if "flowStatus" in data:
        out["flow_status"] = data["flowStatus"]
    else:
        raise DeserializationError("MetaFlowSummary.flow_status required")
    if "flowCategories" in data:
        import capo_socialmessaging.types.meta_flow_category_list

        out["flow_categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["flowCategories"]
            )
        )
    else:
        raise DeserializationError("MetaFlowSummary.flow_categories required")
    if "validationErrors" in data:
        import capo_socialmessaging.types.validation_error_list

        out["validation_errors"] = (
            capo_socialmessaging.types.validation_error_list.deserialize_json(
                data["validationErrors"]
            )
        )
    else:
        raise DeserializationError("MetaFlowSummary.validation_errors required")
    return out
