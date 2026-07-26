"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedContractDurationTerm``."""

from typing import Literal, TypeAlias, cast

"""<p>The unit of measurement for the contract duration value. Currently accepts only <code>Months</code>.</p>"""
ExpectedContractDurationTerm: TypeAlias = Literal["Months",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedContractDurationTerm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExpectedContractDurationTerm:
    return cast(ExpectedContractDurationTerm, data)
