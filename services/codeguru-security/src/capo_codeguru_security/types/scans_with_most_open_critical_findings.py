"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScansWithMostOpenCriticalFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_security.types.scan_name_with_finding_num

ScansWithMostOpenCriticalFindings: TypeAlias = list[
    "capo_codeguru_security.types.scan_name_with_finding_num.ScanNameWithFindingNum"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScansWithMostOpenCriticalFindings) -> list:
    import capo_codeguru_security.types.scan_name_with_finding_num

    out: list = []
    for item in value:
        out.append(
            capo_codeguru_security.types.scan_name_with_finding_num.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ScansWithMostOpenCriticalFindings:
    import capo_codeguru_security.types.scan_name_with_finding_num

    out: ScansWithMostOpenCriticalFindings = []
    for item in data:
        out.append(
            capo_codeguru_security.types.scan_name_with_finding_num.deserialize_json(
                item
            )
        )
    return out
