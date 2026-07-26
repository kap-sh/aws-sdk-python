"""Generated from Smithy shape ``com.amazonaws.mturk#LocaleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.locale

LocaleList: TypeAlias = list["capo_mturk.types.locale.Locale"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocaleList) -> list:
    import capo_mturk.types.locale

    out: list = []
    for item in value:
        out.append(capo_mturk.types.locale.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocaleList:
    import capo_mturk.types.locale

    out: LocaleList = []
    for item in data:
        out.append(capo_mturk.types.locale.deserialize_aws_json_1_1(item))
    return out
