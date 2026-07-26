"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsStatistics``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.external_access_findings_statistics
    import capo_accessanalyzer.types.internal_access_findings_statistics
    import capo_accessanalyzer.types.unused_access_findings_statistics


class _FindingsStatistics_externalAccessFindingsStatistics(TypedDict, closed=True):
    externalAccessFindingsStatistics: "capo_accessanalyzer.types.external_access_findings_statistics.ExternalAccessFindingsStatistics"


class _FindingsStatistics_internalAccessFindingsStatistics(TypedDict, closed=True):
    internalAccessFindingsStatistics: "capo_accessanalyzer.types.internal_access_findings_statistics.InternalAccessFindingsStatistics"


class _FindingsStatistics_unusedAccessFindingsStatistics(TypedDict, closed=True):
    unusedAccessFindingsStatistics: "capo_accessanalyzer.types.unused_access_findings_statistics.UnusedAccessFindingsStatistics"


FindingsStatistics: TypeAlias = (
    _FindingsStatistics_externalAccessFindingsStatistics
    | _FindingsStatistics_internalAccessFindingsStatistics
    | _FindingsStatistics_unusedAccessFindingsStatistics
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingsStatistics) -> dict:
    if "externalAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.external_access_findings_statistics

        return {
            "externalAccessFindingsStatistics": capo_accessanalyzer.types.external_access_findings_statistics.serialize_json(
                value["externalAccessFindingsStatistics"]
            )
        }
    elif "internalAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.internal_access_findings_statistics

        return {
            "internalAccessFindingsStatistics": capo_accessanalyzer.types.internal_access_findings_statistics.serialize_json(
                value["internalAccessFindingsStatistics"]
            )
        }
    elif "unusedAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.unused_access_findings_statistics

        return {
            "unusedAccessFindingsStatistics": capo_accessanalyzer.types.unused_access_findings_statistics.serialize_json(
                value["unusedAccessFindingsStatistics"]
            )
        }
    else:
        raise SerializationError("FindingsStatistics: no variant present")


def deserialize_json(data: dict) -> FindingsStatistics:
    if "externalAccessFindingsStatistics" in data:
        import capo_accessanalyzer.types.external_access_findings_statistics

        return {
            "externalAccessFindingsStatistics": capo_accessanalyzer.types.external_access_findings_statistics.deserialize_json(
                data["externalAccessFindingsStatistics"]
            )
        }
    elif "internalAccessFindingsStatistics" in data:
        import capo_accessanalyzer.types.internal_access_findings_statistics

        return {
            "internalAccessFindingsStatistics": capo_accessanalyzer.types.internal_access_findings_statistics.deserialize_json(
                data["internalAccessFindingsStatistics"]
            )
        }
    elif "unusedAccessFindingsStatistics" in data:
        import capo_accessanalyzer.types.unused_access_findings_statistics

        return {
            "unusedAccessFindingsStatistics": capo_accessanalyzer.types.unused_access_findings_statistics.deserialize_json(
                data["unusedAccessFindingsStatistics"]
            )
        }
    else:
        raise DeserializationError("FindingsStatistics: no recognized variant key")
