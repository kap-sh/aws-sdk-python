"""Generated from Smithy shape ``com.amazonaws.kms#UpdatePrimaryRegionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.region_type


class UpdatePrimaryRegionRequest(TypedDict):
    key_id: "awd_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the current primary key. When the operation completes, this KMS key will be a replica key.</p> <p>Specify the key ID or key ARN of a multi-Region primary key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>mrk-1234abcd12ab34cd56ef1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    primary_region: "awd_sdk_kms.types.region_type.RegionType"
    """<p>The Amazon Web Services Region of the new primary key. Enter the Region ID, such as <code>us-east-1</code> or <code>ap-southeast-2</code>. There must be an existing replica key in this Region. </p> <p>When the operation completes, the multi-Region key in this Region will be the primary key.</p>"""
