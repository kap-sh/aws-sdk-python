"""Generated from Smithy shape ``com.amazonaws.transfer#ListedWebApps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_web_app

ListedWebApps: TypeAlias = list["capo_transfer.types.listed_web_app.ListedWebApp"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedWebApps) -> list:
    import capo_transfer.types.listed_web_app

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_web_app.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedWebApps:
    import capo_transfer.types.listed_web_app

    out: ListedWebApps = []
    for item in data:
        out.append(capo_transfer.types.listed_web_app.deserialize_aws_json_1_1(item))
    return out
