"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransfers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.responsibility_transfer

ResponsibilityTransfers: TypeAlias = list[
    "aws_sdk_organizations.types.responsibility_transfer.ResponsibilityTransfer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransfers) -> list:
    import aws_sdk_organizations.types.responsibility_transfer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.responsibility_transfer.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResponsibilityTransfers:
    import aws_sdk_organizations.types.responsibility_transfer

    out: ResponsibilityTransfers = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.responsibility_transfer.deserialize_aws_json_1_1(
                item
            )
        )
    return out
