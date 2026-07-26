"""Generated from Smithy shape ``com.amazonaws.s3files#ImportDataRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3files.types.import_data_rule

ImportDataRuleList: TypeAlias = list[
    "capo_s3files.types.import_data_rule.ImportDataRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportDataRuleList) -> list:
    import capo_s3files.types.import_data_rule

    out: list = []
    for item in value:
        out.append(capo_s3files.types.import_data_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportDataRuleList:
    import capo_s3files.types.import_data_rule

    out: ImportDataRuleList = []
    for item in data:
        out.append(capo_s3files.types.import_data_rule.deserialize_json(item))
    return out
