from __future__ import annotations
from ._auth._identity import Identity as Identity, Credentials as Credentials
from ._auth._providers import (
    IdentityNotFound as IdentityNotFound,
    IdentityProvider as IdentityProvider,
    ChainedProvider as ChainedProvider,
    CachedProvider as CachedProvider,
    CredentialsProvider as CredentialsProvider,
    StaticAwsCredentialsProvider as StaticAwsCredentialsProvider,
    EnvCredentialsProvider as EnvCredentialsProvider,
    ProfileCredentialsProvider as ProfileCredentialsProvider,
)
from ._auth._signers import Signer as Signer, SigV4Signer as SigV4Signer
from ._services.trent_service import KMSClient as KMSClient
from ._services.async_trent_service import AsyncKMSClient as AsyncKMSClient
