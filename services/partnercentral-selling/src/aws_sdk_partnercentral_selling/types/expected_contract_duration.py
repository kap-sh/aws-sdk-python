"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedContractDuration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.expected_contract_duration_term


class ExpectedContractDuration(TypedDict):
    term: "aws_sdk_partnercentral_selling.types.expected_contract_duration_term.ExpectedContractDurationTerm"
    """<p>The unit of measurement for the contract duration value. Currently accepts only <code>Months</code>.</p>"""
    value: "str"
    """<p>A String representation of the contract duration as an integer, expressed in the unit defined by <code>Term</code>. Valid values range from <code>1</code> to <code>144</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedContractDuration) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.expected_contract_duration_term

    out["Term"] = (
        aws_sdk_partnercentral_selling.types.expected_contract_duration_term.serialize_aws_json_1_0(
            value["term"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedContractDuration:
    out: ExpectedContractDuration = {}  # type: ignore[typeddict-item]
    if "Term" in data:
        import aws_sdk_partnercentral_selling.types.expected_contract_duration_term

        out["term"] = (
            aws_sdk_partnercentral_selling.types.expected_contract_duration_term.deserialize_aws_json_1_0(
                data["Term"]
            )
        )
    else:
        raise DeserializationError("ExpectedContractDuration.term required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ExpectedContractDuration.value required")
    return out
