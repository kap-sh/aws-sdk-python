"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetAutoMergingPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.conflict_resolution
    import aws_sdk_customer_profiles.types.consolidation
    import aws_sdk_customer_profiles.types.double0_to1
    import aws_sdk_customer_profiles.types.name


class GetAutoMergingPreviewRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    consolidation: "aws_sdk_customer_profiles.types.consolidation.Consolidation"
    """<p>A list of matching attributes that represent matching criteria.</p>"""
    conflict_resolution: (
        "aws_sdk_customer_profiles.types.conflict_resolution.ConflictResolution"
    )
    """<p>How the auto-merging process should resolve conflicts between different profiles.</p>"""
    min_allowed_confidence_score_for_merging: NotRequired[
        "aws_sdk_customer_profiles.types.double0_to1.Double0To1"
    ]
    """<p>Minimum confidence score required for profiles within a matching group to be merged during the auto-merge process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutoMergingPreviewRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.consolidation

    out["Consolidation"] = aws_sdk_customer_profiles.types.consolidation.serialize_json(
        value["consolidation"]
    )
    import aws_sdk_customer_profiles.types.conflict_resolution

    out["ConflictResolution"] = (
        aws_sdk_customer_profiles.types.conflict_resolution.serialize_json(
            value["conflict_resolution"]
        )
    )
    if "min_allowed_confidence_score_for_merging" in value:
        out["MinAllowedConfidenceScoreForMerging"] = value[
            "min_allowed_confidence_score_for_merging"
        ]
    return out


def deserialize_json(data: dict) -> GetAutoMergingPreviewRequest:
    out: GetAutoMergingPreviewRequest = {}  # type: ignore[typeddict-item]
    if "Consolidation" in data:
        import aws_sdk_customer_profiles.types.consolidation

        out["consolidation"] = (
            aws_sdk_customer_profiles.types.consolidation.deserialize_json(
                data["Consolidation"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutoMergingPreviewRequest.consolidation required"
        )
    if "ConflictResolution" in data:
        import aws_sdk_customer_profiles.types.conflict_resolution

        out["conflict_resolution"] = (
            aws_sdk_customer_profiles.types.conflict_resolution.deserialize_json(
                data["ConflictResolution"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutoMergingPreviewRequest.conflict_resolution required"
        )
    if "MinAllowedConfidenceScoreForMerging" in data:
        out["min_allowed_confidence_score_for_merging"] = data[
            "MinAllowedConfidenceScoreForMerging"
        ]
    return out
