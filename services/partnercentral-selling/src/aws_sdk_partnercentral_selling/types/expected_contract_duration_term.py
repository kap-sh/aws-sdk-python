"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedContractDurationTerm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

"""<p>The unit of measurement for the contract duration value. Currently accepts only <code>Months</code>.</p>"""
ExpectedContractDurationTerm: TypeAlias = Literal["Months",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Months",))


def serialize_aws_json_1_0(value: ExpectedContractDurationTerm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExpectedContractDurationTerm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExpectedContractDurationTerm value: {data!r}"
        )
    return cast(ExpectedContractDurationTerm, data)
