"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ReservedInstanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.offering_class
    import capo_application_discovery_service.types.purchasing_option
    import capo_application_discovery_service.types.term_length


class ReservedInstanceOptions(TypedDict, closed=True):
    purchasing_option: (
        "capo_application_discovery_service.types.purchasing_option.PurchasingOption"
    )
    """<p> The payment plan to use for your Reserved Instance. </p>"""
    offering_class: (
        "capo_application_discovery_service.types.offering_class.OfferingClass"
    )
    """<p> The flexibility to change the instance types needed for your Reserved Instance. </p>"""
    term_length: "capo_application_discovery_service.types.term_length.TermLength"
    """<p> The preferred duration of the Reserved Instance term. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedInstanceOptions) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.purchasing_option

    out["purchasingOption"] = (
        capo_application_discovery_service.types.purchasing_option.serialize_aws_json_1_1(
            value["purchasing_option"]
        )
    )
    import capo_application_discovery_service.types.offering_class

    out["offeringClass"] = (
        capo_application_discovery_service.types.offering_class.serialize_aws_json_1_1(
            value["offering_class"]
        )
    )
    import capo_application_discovery_service.types.term_length

    out["termLength"] = (
        capo_application_discovery_service.types.term_length.serialize_aws_json_1_1(
            value["term_length"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedInstanceOptions:
    out: ReservedInstanceOptions = {}  # type: ignore[typeddict-item]
    if "purchasingOption" in data:
        import capo_application_discovery_service.types.purchasing_option

        out["purchasing_option"] = (
            capo_application_discovery_service.types.purchasing_option.deserialize_aws_json_1_1(
                data["purchasingOption"]
            )
        )
    else:
        raise DeserializationError("ReservedInstanceOptions.purchasing_option required")
    if "offeringClass" in data:
        import capo_application_discovery_service.types.offering_class

        out["offering_class"] = (
            capo_application_discovery_service.types.offering_class.deserialize_aws_json_1_1(
                data["offeringClass"]
            )
        )
    else:
        raise DeserializationError("ReservedInstanceOptions.offering_class required")
    if "termLength" in data:
        import capo_application_discovery_service.types.term_length

        out["term_length"] = (
            capo_application_discovery_service.types.term_length.deserialize_aws_json_1_1(
                data["termLength"]
            )
        )
    else:
        raise DeserializationError("ReservedInstanceOptions.term_length required")
    return out
