"""Generated from Smithy shape ``com.amazonaws.appstream#EntitledApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.entitled_application

EntitledApplicationList: TypeAlias = list[
    "capo_appstream.types.entitled_application.EntitledApplication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitledApplicationList) -> list:
    import capo_appstream.types.entitled_application

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.entitled_application.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitledApplicationList:
    import capo_appstream.types.entitled_application

    out: EntitledApplicationList = []
    for item in data:
        out.append(
            capo_appstream.types.entitled_application.deserialize_aws_json_1_1(item)
        )
    return out
