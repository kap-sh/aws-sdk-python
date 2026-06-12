"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateRecommendationStatusRequestEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.boolean_optional
    import aws_sdk_resiliencehub.types.entity_name255
    import aws_sdk_resiliencehub.types.exclude_recommendation_reason
    import aws_sdk_resiliencehub.types.spec_reference_id
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.update_recommendation_status_item


class UpdateRecommendationStatusRequestEntry(TypedDict):
    entry_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>An identifier for an entry in this batch that is used to communicate the result.</p> <note> <p>The <code>entryId</code>s of a batch request need to be unique within a request.</p> </note>"""
    reference_id: "aws_sdk_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier of the operational recommendation item.</p>"""
    item: NotRequired[
        "aws_sdk_resiliencehub.types.update_recommendation_status_item.UpdateRecommendationStatusItem"
    ]
    """<p>The operational recommendation item.</p>"""
    excluded: "aws_sdk_resiliencehub.types.boolean_optional.BooleanOptional"
    """<p>Indicates if the operational recommendation needs to be excluded. If set to True, the operational recommendation will be excluded.</p>"""
    app_component_id: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name255.EntityName255"
    ]
    """<p>Indicates the identifier of the AppComponent.</p>"""
    exclude_reason: NotRequired[
        "aws_sdk_resiliencehub.types.exclude_recommendation_reason.ExcludeRecommendationReason"
    ]
    """<p>Indicates the reason for excluding an operational recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationStatusRequestEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    out["referenceId"] = value["reference_id"]
    if "item" in value:
        import aws_sdk_resiliencehub.types.update_recommendation_status_item

        out["item"] = (
            aws_sdk_resiliencehub.types.update_recommendation_status_item.serialize_json(
                value["item"]
            )
        )
    out["excluded"] = value["excluded"]
    if "app_component_id" in value:
        out["appComponentId"] = value["app_component_id"]
    if "exclude_reason" in value:
        import aws_sdk_resiliencehub.types.exclude_recommendation_reason

        out["excludeReason"] = (
            aws_sdk_resiliencehub.types.exclude_recommendation_reason.serialize_json(
                value["exclude_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommendationStatusRequestEntry:
    out: UpdateRecommendationStatusRequestEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "UpdateRecommendationStatusRequestEntry.entry_id required"
        )
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError(
            "UpdateRecommendationStatusRequestEntry.reference_id required"
        )
    if "item" in data:
        import aws_sdk_resiliencehub.types.update_recommendation_status_item

        out["item"] = (
            aws_sdk_resiliencehub.types.update_recommendation_status_item.deserialize_json(
                data["item"]
            )
        )
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    else:
        raise DeserializationError(
            "UpdateRecommendationStatusRequestEntry.excluded required"
        )
    if "appComponentId" in data:
        out["app_component_id"] = data["appComponentId"]
    if "excludeReason" in data:
        import aws_sdk_resiliencehub.types.exclude_recommendation_reason

        out["exclude_reason"] = (
            aws_sdk_resiliencehub.types.exclude_recommendation_reason.deserialize_json(
                data["excludeReason"]
            )
        )
    return out
