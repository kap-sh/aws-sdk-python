"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ModuleParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.no_bid_module_parameters
    import capo_rtbfabric.types.open_rtb_attribute_module_parameters
    import capo_rtbfabric.types.rate_limiter_module_parameters


class _ModuleParameters_noBid(TypedDict, closed=True):
    noBid: "capo_rtbfabric.types.no_bid_module_parameters.NoBidModuleParameters"


class _ModuleParameters_openRtbAttribute(TypedDict, closed=True):
    openRtbAttribute: "capo_rtbfabric.types.open_rtb_attribute_module_parameters.OpenRtbAttributeModuleParameters"


class _ModuleParameters_rateLimiter(TypedDict, closed=True):
    rateLimiter: "capo_rtbfabric.types.rate_limiter_module_parameters.RateLimiterModuleParameters"


ModuleParameters: TypeAlias = (
    _ModuleParameters_noBid
    | _ModuleParameters_openRtbAttribute
    | _ModuleParameters_rateLimiter
)


# --- restJson1 ser/de ---
def serialize_json(value: ModuleParameters) -> dict:
    if "noBid" in value:
        import capo_rtbfabric.types.no_bid_module_parameters

        return {
            "noBid": capo_rtbfabric.types.no_bid_module_parameters.serialize_json(
                value["noBid"]
            )
        }
    elif "openRtbAttribute" in value:
        import capo_rtbfabric.types.open_rtb_attribute_module_parameters

        return {
            "openRtbAttribute": capo_rtbfabric.types.open_rtb_attribute_module_parameters.serialize_json(
                value["openRtbAttribute"]
            )
        }
    elif "rateLimiter" in value:
        import capo_rtbfabric.types.rate_limiter_module_parameters

        return {
            "rateLimiter": capo_rtbfabric.types.rate_limiter_module_parameters.serialize_json(
                value["rateLimiter"]
            )
        }
    else:
        raise SerializationError("ModuleParameters: no variant present")


def deserialize_json(data: dict) -> ModuleParameters:
    if "noBid" in data:
        import capo_rtbfabric.types.no_bid_module_parameters

        return {
            "noBid": capo_rtbfabric.types.no_bid_module_parameters.deserialize_json(
                data["noBid"]
            )
        }
    elif "openRtbAttribute" in data:
        import capo_rtbfabric.types.open_rtb_attribute_module_parameters

        return {
            "openRtbAttribute": capo_rtbfabric.types.open_rtb_attribute_module_parameters.deserialize_json(
                data["openRtbAttribute"]
            )
        }
    elif "rateLimiter" in data:
        import capo_rtbfabric.types.rate_limiter_module_parameters

        return {
            "rateLimiter": capo_rtbfabric.types.rate_limiter_module_parameters.deserialize_json(
                data["rateLimiter"]
            )
        }
    else:
        raise DeserializationError("ModuleParameters: no recognized variant key")
