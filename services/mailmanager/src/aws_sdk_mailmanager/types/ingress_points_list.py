"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_point

IngressPointsList: TypeAlias = list[
    "aws_sdk_mailmanager.types.ingress_point.IngressPoint"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointsList) -> list:
    import aws_sdk_mailmanager.types.ingress_point

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.ingress_point.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> IngressPointsList:
    import aws_sdk_mailmanager.types.ingress_point

    out: IngressPointsList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.ingress_point.deserialize_aws_json_1_0(item)
        )
    return out
