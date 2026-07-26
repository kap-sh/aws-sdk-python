"""Generated from Smithy shape ``com.amazonaws.securityhub#ImportFindingsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.import_findings_error

ImportFindingsErrorList: TypeAlias = list[
    "capo_securityhub.types.import_findings_error.ImportFindingsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFindingsErrorList) -> list:
    import capo_securityhub.types.import_findings_error

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.import_findings_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportFindingsErrorList:
    import capo_securityhub.types.import_findings_error

    out: ImportFindingsErrorList = []
    for item in data:
        out.append(capo_securityhub.types.import_findings_error.deserialize_json(item))
    return out
