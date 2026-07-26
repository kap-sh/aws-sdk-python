"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#SyncResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_arn
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.sync_action


class SyncResourceResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the application.</p>"""
    resource_arn: NotRequired["capo_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    action_taken: NotRequired[
        "capo_service_catalog_appregistry.types.sync_action.SyncAction"
    ]
    """<p>The results of the output if an application is associated with an ARN value, which could be <code>syncStarted</code> or None.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "action_taken" in value:
        import capo_service_catalog_appregistry.types.sync_action

        out["actionTaken"] = (
            capo_service_catalog_appregistry.types.sync_action.serialize_json(
                value["action_taken"]
            )
        )
    return out


def deserialize_json(data: dict) -> SyncResourceResponse:
    out: SyncResourceResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "actionTaken" in data:
        import capo_service_catalog_appregistry.types.sync_action

        out["action_taken"] = (
            capo_service_catalog_appregistry.types.sync_action.deserialize_json(
                data["actionTaken"]
            )
        )
    return out
