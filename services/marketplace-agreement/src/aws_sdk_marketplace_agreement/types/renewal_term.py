"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RenewalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.renewal_term_configuration
    import aws_sdk_marketplace_agreement.types.term_id
    import aws_sdk_marketplace_agreement.types.unversioned_term_type


class RenewalTerm(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated. </p>"""
    id: NotRequired["aws_sdk_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    configuration: NotRequired[
        "aws_sdk_marketplace_agreement.types.renewal_term_configuration.RenewalTermConfiguration"
    ]
    """<p>Additional parameters specified by the acceptor while accepting the term.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RenewalTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "configuration" in value:
        import aws_sdk_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            aws_sdk_marketplace_agreement.types.renewal_term_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RenewalTerm:
    out: RenewalTerm = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "configuration" in data:
        import aws_sdk_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            aws_sdk_marketplace_agreement.types.renewal_term_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out
