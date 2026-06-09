"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.creation_date_condition
    import aws_sdk_ec2.types.deprecation_time_condition
    import aws_sdk_ec2.types.image_name_list
    import aws_sdk_ec2.types.image_provider_list
    import aws_sdk_ec2.types.marketplace_product_code_list


class ImageCriterion(TypedDict):
    image_providers: NotRequired[
        "aws_sdk_ec2.types.image_provider_list.ImageProviderList"
    ]
    """<p>The image providers whose images are allowed.</p> <p>Possible values:</p> <ul> <li> <p> <code>amazon</code>: Allow AMIs created by Amazon or verified providers.</p> </li> <li> <p> <code>aws-marketplace</code>: Allow AMIs created by verified providers in the Amazon Web Services Marketplace.</p> </li> <li> <p> <code>aws-backup-vault</code>: Allow AMIs created by Amazon Web Services Backup. </p> </li> <li> <p>12-digit account ID: Allow AMIs created by this account. One or more account IDs can be specified.</p> </li> <li> <p> <code>none</code>: Allow AMIs created by your own account only.</p> </li> </ul> <p>Maximum: 200 values</p>"""
    marketplace_product_codes: NotRequired[
        "aws_sdk_ec2.types.marketplace_product_code_list.MarketplaceProductCodeList"
    ]
    """<p>The Amazon Web Services Marketplace product codes for allowed images.</p> <p>Length: 1-25 characters</p> <p>Valid characters: Letters (<code>A–Z, a–z</code>) and numbers (<code>0–9</code>)</p> <p>Maximum: 50 values</p>"""
    image_names: NotRequired["aws_sdk_ec2.types.image_name_list.ImageNameList"]
    """<p>The names of allowed images. Names can include wildcards (<code>?</code> and <code>*</code>).</p> <p>Length: 1–128 characters. With <code>?</code>, the minimum is 3 characters.</p> <p>Valid characters:</p> <ul> <li> <p>Letters: <code>A–Z, a–z</code> </p> </li> <li> <p>Numbers: <code>0–9</code> </p> </li> <li> <p>Special characters: <code>( ) [ ] . / - ' @ _ * ?</code> </p> </li> <li> <p>Spaces</p> </li> </ul> <p>Maximum: 50 values</p>"""
    deprecation_time_condition: NotRequired[
        "aws_sdk_ec2.types.deprecation_time_condition.DeprecationTimeCondition"
    ]
    """<p>The maximum period since deprecation for allowed images.</p>"""
    creation_date_condition: NotRequired[
        "aws_sdk_ec2.types.creation_date_condition.CreationDateCondition"
    ]
    """<p>The maximum age for allowed images.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_providers" in value:
        import aws_sdk_ec2.types.image_provider_list

        aws_sdk_ec2.types.image_provider_list.serialize_ec2_query(
            value["image_providers"], pairs, f"{prefix}.ImageProviderSet"
        )
    if "marketplace_product_codes" in value:
        import aws_sdk_ec2.types.marketplace_product_code_list

        aws_sdk_ec2.types.marketplace_product_code_list.serialize_ec2_query(
            value["marketplace_product_codes"],
            pairs,
            f"{prefix}.MarketplaceProductCodeSet",
        )
    if "image_names" in value:
        import aws_sdk_ec2.types.image_name_list

        aws_sdk_ec2.types.image_name_list.serialize_ec2_query(
            value["image_names"], pairs, f"{prefix}.ImageNameSet"
        )
    if "deprecation_time_condition" in value:
        import aws_sdk_ec2.types.deprecation_time_condition

        aws_sdk_ec2.types.deprecation_time_condition.serialize_ec2_query(
            value["deprecation_time_condition"],
            pairs,
            f"{prefix}.DeprecationTimeCondition",
        )
    if "creation_date_condition" in value:
        import aws_sdk_ec2.types.creation_date_condition

        aws_sdk_ec2.types.creation_date_condition.serialize_ec2_query(
            value["creation_date_condition"], pairs, f"{prefix}.CreationDateCondition"
        )


def deserialize_ec2_query(el: Element) -> ImageCriterion:
    out: ImageCriterion = {}  # type: ignore[typeddict-item]
    if el.find("ImageProviderSet") is not None:
        import aws_sdk_ec2.types.image_provider_list

        out["image_providers"] = (
            aws_sdk_ec2.types.image_provider_list.deserialize_ec2_query(
                el, "ImageProviderSet"
            )
        )
    if el.find("MarketplaceProductCodeSet") is not None:
        import aws_sdk_ec2.types.marketplace_product_code_list

        out["marketplace_product_codes"] = (
            aws_sdk_ec2.types.marketplace_product_code_list.deserialize_ec2_query(
                el, "MarketplaceProductCodeSet"
            )
        )
    if el.find("ImageNameSet") is not None:
        import aws_sdk_ec2.types.image_name_list

        out["image_names"] = aws_sdk_ec2.types.image_name_list.deserialize_ec2_query(
            el, "ImageNameSet"
        )
    child_deprecation_time_condition = el.find("DeprecationTimeCondition")
    if child_deprecation_time_condition is not None:
        import aws_sdk_ec2.types.deprecation_time_condition

        out["deprecation_time_condition"] = (
            aws_sdk_ec2.types.deprecation_time_condition.deserialize_ec2_query(
                child_deprecation_time_condition
            )
        )
    child_creation_date_condition = el.find("CreationDateCondition")
    if child_creation_date_condition is not None:
        import aws_sdk_ec2.types.creation_date_condition

        out["creation_date_condition"] = (
            aws_sdk_ec2.types.creation_date_condition.deserialize_ec2_query(
                child_creation_date_condition
            )
        )
    return out
