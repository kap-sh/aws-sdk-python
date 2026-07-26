"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeAgreementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_agreement


class DescribeAgreementResponse(TypedDict, closed=True):
    agreement: "capo_transfer.types.described_agreement.DescribedAgreement"
    """<p>The details for the specified agreement, returned as a <code>DescribedAgreement</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgreementResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.described_agreement

    out["Agreement"] = capo_transfer.types.described_agreement.serialize_aws_json_1_1(
        value["agreement"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgreementResponse:
    out: DescribeAgreementResponse = {}  # type: ignore[typeddict-item]
    if "Agreement" in data:
        import capo_transfer.types.described_agreement

        out["agreement"] = (
            capo_transfer.types.described_agreement.deserialize_aws_json_1_1(
                data["Agreement"]
            )
        )
    else:
        raise DeserializationError("DescribeAgreementResponse.agreement required")
    return out
