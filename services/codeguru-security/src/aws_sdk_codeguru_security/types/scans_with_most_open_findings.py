"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScansWithMostOpenFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.scan_name_with_finding_num

ScansWithMostOpenFindings: TypeAlias = list[
    "aws_sdk_codeguru_security.types.scan_name_with_finding_num.ScanNameWithFindingNum"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScansWithMostOpenFindings) -> list:
    import aws_sdk_codeguru_security.types.scan_name_with_finding_num

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_security.types.scan_name_with_finding_num.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ScansWithMostOpenFindings:
    import aws_sdk_codeguru_security.types.scan_name_with_finding_num

    out: ScansWithMostOpenFindings = []
    for item in data:
        out.append(
            aws_sdk_codeguru_security.types.scan_name_with_finding_num.deserialize_json(
                item
            )
        )
    return out
