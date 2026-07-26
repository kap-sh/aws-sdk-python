"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#GetRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.expires_at
    import capo_sagemaker_featurestore_runtime.types.record


class GetRecordResponse(TypedDict, closed=True):
    record: NotRequired["capo_sagemaker_featurestore_runtime.types.record.Record"]
    """<p>The record you requested. A list of <code>FeatureValues</code>.</p>"""
    expires_at: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.expires_at.ExpiresAt"
    ]
    """<p>The <code>ExpiresAt</code> ISO string of the requested record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecordResponse) -> dict:
    out: dict = {}
    if "record" in value:
        import capo_sagemaker_featurestore_runtime.types.record

        out["Record"] = capo_sagemaker_featurestore_runtime.types.record.serialize_json(
            value["record"]
        )
    if "expires_at" in value:
        out["ExpiresAt"] = value["expires_at"]
    return out


def deserialize_json(data: dict) -> GetRecordResponse:
    out: GetRecordResponse = {}  # type: ignore[typeddict-item]
    if "Record" in data:
        import capo_sagemaker_featurestore_runtime.types.record

        out["record"] = (
            capo_sagemaker_featurestore_runtime.types.record.deserialize_json(
                data["Record"]
            )
        )
    if "ExpiresAt" in data:
        out["expires_at"] = data["ExpiresAt"]
    return out
