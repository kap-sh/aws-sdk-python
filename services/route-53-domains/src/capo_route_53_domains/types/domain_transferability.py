"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainTransferability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.transferable


class DomainTransferability(TypedDict, closed=True):
    transferable: NotRequired["capo_route_53_domains.types.transferable.Transferable"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainTransferability) -> dict:
    out: dict = {}
    if "transferable" in value:
        import capo_route_53_domains.types.transferable

        out["Transferable"] = (
            capo_route_53_domains.types.transferable.serialize_aws_json_1_1(
                value["transferable"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainTransferability:
    out: DomainTransferability = {}  # type: ignore[typeddict-item]
    if "Transferable" in data:
        import capo_route_53_domains.types.transferable

        out["transferable"] = (
            capo_route_53_domains.types.transferable.deserialize_aws_json_1_1(
                data["Transferable"]
            )
        )
    return out
