"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUnprocessedAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.unprocessed_account

__listOfUnprocessedAccount: TypeAlias = list[
    "aws_sdk_macie2.types.unprocessed_account.UnprocessedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUnprocessedAccount) -> list:
    import aws_sdk_macie2.types.unprocessed_account

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.unprocessed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUnprocessedAccount:
    import aws_sdk_macie2.types.unprocessed_account

    out: __listOfUnprocessedAccount = []
    for item in data:
        out.append(aws_sdk_macie2.types.unprocessed_account.deserialize_json(item))
    return out
