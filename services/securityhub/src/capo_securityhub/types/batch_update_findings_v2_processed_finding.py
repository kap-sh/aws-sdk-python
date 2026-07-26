"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2ProcessedFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.ocsf_finding_identifier


class BatchUpdateFindingsV2ProcessedFinding(TypedDict, closed=True):
    finding_identifier: NotRequired[
        "capo_securityhub.types.ocsf_finding_identifier.OcsfFindingIdentifier"
    ]
    """<p>The finding identifier of a processed finding.</p>"""
    metadata_uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The metadata.uid of a processed finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2ProcessedFinding) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import capo_securityhub.types.ocsf_finding_identifier

        out["FindingIdentifier"] = (
            capo_securityhub.types.ocsf_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "metadata_uid" in value:
        out["MetadataUid"] = value["metadata_uid"]
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsV2ProcessedFinding:
    out: BatchUpdateFindingsV2ProcessedFinding = {}  # type: ignore[typeddict-item]
    if "FindingIdentifier" in data:
        import capo_securityhub.types.ocsf_finding_identifier

        out["finding_identifier"] = (
            capo_securityhub.types.ocsf_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if "MetadataUid" in data:
        out["metadata_uid"] = data["MetadataUid"]
    return out
