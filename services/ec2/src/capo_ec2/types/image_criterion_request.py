"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.creation_date_condition_request
    import capo_ec2.types.deprecation_time_condition_request
    import capo_ec2.types.image_name_criteria_request_list
    import capo_ec2.types.image_provider_request_list
    import capo_ec2.types.marketplace_product_code_request_list


class ImageCriterionRequest(TypedDict, closed=True):
    image_providers: NotRequired[
        "capo_ec2.types.image_provider_request_list.ImageProviderRequestList"
    ]
    """<p>The image providers whose images are allowed.</p> <p>Possible values:</p> <ul> <li> <p> <code>amazon</code>: Allow AMIs created by Amazon or verified providers.</p> </li> <li> <p> <code>aws-marketplace</code>: Allow AMIs created by verified providers in the Amazon Web Services Marketplace.</p> </li> <li> <p> <code>aws-backup-vault</code>: Allow AMIs created by Amazon Web Services Backup. </p> </li> <li> <p>12-digit account ID: Allow AMIs created by the specified accounts. One or more account IDs can be specified.</p> </li> <li> <p> <code>none</code>: Allow AMIs created by your own account only. When <code>none</code> is specified, no other values can be specified.</p> </li> </ul> <p>Maximum: 200 values</p>"""
    marketplace_product_codes: NotRequired[
        "capo_ec2.types.marketplace_product_code_request_list.MarketplaceProductCodeRequestList"
    ]
    """<p>The Amazon Web Services Marketplace product codes for allowed images.</p> <p>Length: 1-25 characters</p> <p>Valid characters: Letters (<code>A–Z, a–z</code>) and numbers (<code>0–9</code>)</p> <p>Maximum: 50 values</p>"""
    image_names: NotRequired[
        "capo_ec2.types.image_name_criteria_request_list.ImageNameCriteriaRequestList"
    ]
    """<p>The names of allowed images. Names can include wildcards (<code>?</code> and <code>*</code>).</p> <p>Length: 1–128 characters. With <code>?</code>, the minimum is 3 characters.</p> <p>Valid characters:</p> <ul> <li> <p>Letters: <code>A–Z, a–z</code> </p> </li> <li> <p>Numbers: <code>0–9</code> </p> </li> <li> <p>Special characters: <code>( ) [ ] . / - ' @ _ * ?</code> </p> </li> <li> <p>Spaces</p> </li> </ul> <p>Maximum: 50 values</p>"""
    deprecation_time_condition: NotRequired[
        "capo_ec2.types.deprecation_time_condition_request.DeprecationTimeConditionRequest"
    ]
    """<p>The maximum period since deprecation for allowed images.</p>"""
    creation_date_condition: NotRequired[
        "capo_ec2.types.creation_date_condition_request.CreationDateConditionRequest"
    ]
    """<p>The maximum age for allowed images.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_providers" in value:
        import capo_ec2.types.image_provider_request_list

        capo_ec2.types.image_provider_request_list.serialize_ec2_query(
            value["image_providers"], pairs, f"{key_prefix}ImageProviders"
        )
    if "marketplace_product_codes" in value:
        import capo_ec2.types.marketplace_product_code_request_list

        capo_ec2.types.marketplace_product_code_request_list.serialize_ec2_query(
            value["marketplace_product_codes"],
            pairs,
            f"{key_prefix}MarketplaceProductCodes",
        )
    if "image_names" in value:
        import capo_ec2.types.image_name_criteria_request_list

        capo_ec2.types.image_name_criteria_request_list.serialize_ec2_query(
            value["image_names"], pairs, f"{key_prefix}ImageNames"
        )
    if "deprecation_time_condition" in value:
        import capo_ec2.types.deprecation_time_condition_request

        capo_ec2.types.deprecation_time_condition_request.serialize_ec2_query(
            value["deprecation_time_condition"],
            pairs,
            f"{key_prefix}DeprecationTimeCondition",
        )
    if "creation_date_condition" in value:
        import capo_ec2.types.creation_date_condition_request

        capo_ec2.types.creation_date_condition_request.serialize_ec2_query(
            value["creation_date_condition"],
            pairs,
            f"{key_prefix}CreationDateCondition",
        )


def deserialize_ec2_query(el: Element) -> ImageCriterionRequest:
    out: ImageCriterionRequest = {}  # type: ignore[typeddict-item]
    if el.find("ImageProviders") is not None:
        import capo_ec2.types.image_provider_request_list

        out["image_providers"] = (
            capo_ec2.types.image_provider_request_list.deserialize_ec2_query(
                el, "ImageProviders"
            )
        )
    if el.find("MarketplaceProductCodes") is not None:
        import capo_ec2.types.marketplace_product_code_request_list

        out["marketplace_product_codes"] = (
            capo_ec2.types.marketplace_product_code_request_list.deserialize_ec2_query(
                el, "MarketplaceProductCodes"
            )
        )
    if el.find("ImageNames") is not None:
        import capo_ec2.types.image_name_criteria_request_list

        out["image_names"] = (
            capo_ec2.types.image_name_criteria_request_list.deserialize_ec2_query(
                el, "ImageNames"
            )
        )
    child_deprecation_time_condition = el.find("DeprecationTimeCondition")
    if child_deprecation_time_condition is not None:
        import capo_ec2.types.deprecation_time_condition_request

        out["deprecation_time_condition"] = (
            capo_ec2.types.deprecation_time_condition_request.deserialize_ec2_query(
                child_deprecation_time_condition
            )
        )
    child_creation_date_condition = el.find("CreationDateCondition")
    if child_creation_date_condition is not None:
        import capo_ec2.types.creation_date_condition_request

        out["creation_date_condition"] = (
            capo_ec2.types.creation_date_condition_request.deserialize_ec2_query(
                child_creation_date_condition
            )
        )
    return out
